import structlog
logger=structlog.get_logger()
logger.info(
    'student_requested',
    student_id=101,
    user_id=500
)



