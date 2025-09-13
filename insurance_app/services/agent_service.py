import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from insurance_app import models
from insurance_app.schemas import agent_schema

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def create_agent(db: Session, agent: agent_schema.AgentCreate):
    try:
        db_agent = models.Agent(**agent.dict())
        db.add(db_agent)
        db.commit()
        db.refresh(db_agent)
        return db_agent
    except SQLAlchemyError as e:
        logger.error(f"Database error during agent creation: {e}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create agent"
        )
    except Exception as e:
        logger.error(f"Unexpected error during agent creation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error occurred"
        )

def get_all_agents(db: Session):
    try:
        return db.query(models.Agent).all()
    except SQLAlchemyError as e:
        logger.error(f"Database error during fetching all agents: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch agents"
        )

def get_agent_by_id(db: Session, agent_id: int):
    try:
        agent = db.query(models.Agent).filter(models.Agent.id == agent_id).first()
        if not agent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agent not found"
            )
        return agent
    except SQLAlchemyError as e:
        logger.error(f"Database error during fetching agent by ID: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch agent"
        )

def update_agent(db: Session, agent_id: int, agent_data: agent_schema.AgentUpdate):
    try:
        agent = db.query(models.Agent).filter(models.Agent.id == agent_id).first()
        if not agent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agent not found"
            )
        for key, value in agent_data.dict(exclude_unset=True).items():
            setattr(agent, key, value)
        db.commit()
        db.refresh(agent)
        return agent
    except SQLAlchemyError as e:
        logger.error(f"Database error during agent update: {e}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update agent"
        )
    except Exception as e:
        logger.error(f"Unexpected error during agent update: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error occurred"
        )

def delete_agent(db: Session, agent_id: int):
    try:
        agent = db.query(models.Agent).filter(models.Agent.id == agent_id).first()
        if not agent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agent not found"
            )
        db.delete(agent)
        db.commit()
    except SQLAlchemyError as e:
        logger.error(f"Database error during agent deletion: {e}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete agent"
        )
    except Exception as e:
        logger.error(f"Unexpected error during agent deletion: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error occurred"
        )




