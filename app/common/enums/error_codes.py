

from enum import Enum
from fastapi import status


class BaseErrorCode:
    def __init__(self, http_status, code, message):
        self.http_status = http_status
        self.code = code
        self.message = message

    def message_text(self, messages_map):
        return messages_map.get(self, "Unknown error occurred")



class CommonErrorCode(BaseErrorCode, Enum):
    NOT_FOUND = (status.HTTP_404_NOT_FOUND, 404, "NOT_FOUND")
    ALREADY_EXISTS = (status.HTTP_409_CONFLICT, 409, "ALREADY_EXISTS")
    VALIDATION_ERROR = (status.HTTP_422_UNPROCESSABLE_ENTITY, 422, "VALIDATION_ERROR")
    BAD_REQUEST = (status.HTTP_400_BAD_REQUEST, 400, "BAD_REQUEST")
    UNAUTHORIZED = (status.HTTP_401_UNAUTHORIZED, 401, "UNAUTHORIZED")
    FORBIDDEN = (status.HTTP_403_FORBIDDEN, 403, "FORBIDDEN")
    INTERNAL_SERVER_ERROR = (status.HTTP_500_INTERNAL_SERVER_ERROR, 500, "INTERNAL_SERVER_ERROR")
    DATABASE_ERROR = (status.HTTP_500_INTERNAL_SERVER_ERROR, 500, "DATABASE_ERROR")
    EXTERNAL_SERVICE_ERROR = (status.HTTP_502_BAD_GATEWAY, 502, "EXTERNAL_SERVICE_ERROR")
    RATE_LIMIT_EXCEEDED = (status.HTTP_429_TOO_MANY_REQUESTS, 429, "RATE_LIMIT_EXCEEDED")

class AuthErrorCode( Enum):
    """Authentication and Authorization error codes"""
    INVALID_CREDENTIALS = "AUTH_INVALID_CREDENTIALS"
    TOKEN_EXPIRED = "AUTH_TOKEN_EXPIRED"
    TOKEN_INVALID = "AUTH_TOKEN_INVALID"
    TOKEN_MISSING = "AUTH_TOKEN_MISSING"
    INSUFFICIENT_PERMISSIONS = "AUTH_INSUFFICIENT_PERMISSIONS"
    ACCOUNT_DISABLED = "AUTH_ACCOUNT_DISABLED"
    ACCOUNT_NOT_VERIFIED = "AUTH_ACCOUNT_NOT_VERIFIED"
    PASSWORD_TOO_WEAK = "AUTH_PASSWORD_TOO_WEAK"
    PASSWORD_MISMATCH = "AUTH_PASSWORD_MISMATCH"


class UserErrorCode(BaseErrorCode, Enum):
    USER_NOT_FOUND = (status.HTTP_404_NOT_FOUND, 404, "USER_NOT_FOUND")
    USER_ALREADY_EXISTS = (status.HTTP_409_CONFLICT, 409, "USER_ALREADY_EXISTS")
    USER_EMAIL_EXISTS = (status.HTTP_409_CONFLICT, 409, "USER_EMAIL_EXISTS")
    USER_PHONE_EXISTS = (status.HTTP_409_CONFLICT, 409, "USER_PHONE_EXISTS")
    USER_INVALID_EMAIL = (status.HTTP_400_BAD_REQUEST, 400, "USER_INVALID_EMAIL")
    USER_INVALID_PHONE = (status.HTTP_400_BAD_REQUEST, 400, "USER_INVALID_PHONE")
    USER_UPDATE_FAILED = (status.HTTP_500_INTERNAL_SERVER_ERROR, 500, "USER_UPDATE_FAILED")
    USER_DELETE_FAILED = (status.HTTP_500_INTERNAL_SERVER_ERROR, 500, "USER_DELETE_FAILED")


class AppointmentErrorCode( Enum):
    APPOINTMENT_NOT_FOUND = "APPOINTMENT_NOT_FOUND"
    APPOINTMENT_CONFLICT = "APPOINTMENT_CONFLICT"
    APPOINTMENT_INVALID_TIME = "APPOINTMENT_INVALID_TIME"
    APPOINTMENT_PAST_DATE = "APPOINTMENT_PAST_DATE"
    APPOINTMENT_ALREADY_CANCELLED = "APPOINTMENT_ALREADY_CANCELLED"
    APPOINTMENT_ALREADY_COMPLETED = "APPOINTMENT_ALREADY_COMPLETED"
    APPOINTMENT_CANNOT_CANCEL = "APPOINTMENT_CANNOT_CANCEL"
    APPOINTMENT_CANNOT_RESCHEDULE = "APPOINTMENT_CANNOT_RESCHEDULE"
    APPOINTMENT_SLOT_UNAVAILABLE = "APPOINTMENT_SLOT_UNAVAILABLE"
    APPOINTMENT_DURATION_INVALID = "APPOINTMENT_DURATION_INVALID"


class BookingErrorCode( Enum):
    BOOKING_NOT_FOUND = "BOOKING_NOT_FOUND"
    BOOKING_ALREADY_EXISTS = "BOOKING_ALREADY_EXISTS"
    BOOKING_PAYMENT_FAILED = "BOOKING_PAYMENT_FAILED"
    BOOKING_REFUND_FAILED = "BOOKING_REFUND_FAILED"
    BOOKING_INVALID_STATUS = "BOOKING_INVALID_STATUS"


class PaymentErrorCode( Enum):
    PAYMENT_NOT_FOUND = "PAYMENT_NOT_FOUND"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    PAYMENT_ALREADY_PROCESSED = "PAYMENT_ALREADY_PROCESSED"
    PAYMENT_INVALID_AMOUNT = "PAYMENT_INVALID_AMOUNT"
    PAYMENT_METHOD_INVALID = "PAYMENT_METHOD_INVALID"
    PAYMENT_GATEWAY_ERROR = "PAYMENT_GATEWAY_ERROR"


class NotificationErrorCode( Enum):
    NOTIFICATION_SEND_FAILED = "NOTIFICATION_SEND_FAILED"
    NOTIFICATION_INVALID_TEMPLATE = "NOTIFICATION_INVALID_TEMPLATE"
    NOTIFICATION_INVALID_RECIPIENT = "NOTIFICATION_INVALID_RECIPIENT"




# Error messages mapping
ERROR_MESSAGES = {
    CommonErrorCode.NOT_FOUND: "Resource not found",
    CommonErrorCode.ALREADY_EXISTS: "Resource already exists",
    CommonErrorCode.VALIDATION_ERROR: "Validation error",
    CommonErrorCode.BAD_REQUEST: "Bad request",
    CommonErrorCode.UNAUTHORIZED: "Authentication required",
    CommonErrorCode.FORBIDDEN: "Access forbidden",
    CommonErrorCode.INTERNAL_SERVER_ERROR: "Internal server error",
    CommonErrorCode.DATABASE_ERROR: "Database error occurred",
    CommonErrorCode.EXTERNAL_SERVICE_ERROR: "External service error",
    CommonErrorCode.RATE_LIMIT_EXCEEDED: "Rate limit exceeded",

    # Auth errors
    AuthErrorCode.INVALID_CREDENTIALS: "Invalid email or password",
    AuthErrorCode.TOKEN_EXPIRED: "Authentication token has expired",
    AuthErrorCode.TOKEN_INVALID: "Invalid authentication token",
    AuthErrorCode.TOKEN_MISSING: "Authentication token is missing",
    AuthErrorCode.INSUFFICIENT_PERMISSIONS: "Insufficient permissions",
    AuthErrorCode.ACCOUNT_DISABLED: "Account has been disabled",
    AuthErrorCode.ACCOUNT_NOT_VERIFIED: "Account not verified",
    AuthErrorCode.PASSWORD_TOO_WEAK: "Password is too weak",
    AuthErrorCode.PASSWORD_MISMATCH: "Passwords do not match",

    # User errors
    UserErrorCode.USER_NOT_FOUND: "User not found",
    UserErrorCode.USER_ALREADY_EXISTS: "User already exists",
    UserErrorCode.USER_EMAIL_EXISTS: "Email already registered",
    UserErrorCode.USER_PHONE_EXISTS: "Phone number already registered",
    UserErrorCode.USER_INVALID_EMAIL: "Invalid email format",
    UserErrorCode.USER_INVALID_PHONE: "Invalid phone number",
    UserErrorCode.USER_UPDATE_FAILED: "Failed to update user",
    UserErrorCode.USER_DELETE_FAILED: "Failed to delete user",

    # Appointment errors
    AppointmentErrorCode.APPOINTMENT_NOT_FOUND: "Appointment not found",
    AppointmentErrorCode.APPOINTMENT_CONFLICT: "Appointment time slot conflicts with existing appointment",
    AppointmentErrorCode.APPOINTMENT_INVALID_TIME: "Invalid appointment time",
    AppointmentErrorCode.APPOINTMENT_PAST_DATE: "Cannot book appointment in the past",
    AppointmentErrorCode.APPOINTMENT_ALREADY_CANCELLED: "Appointment already cancelled",
    AppointmentErrorCode.APPOINTMENT_ALREADY_COMPLETED: "Appointment already completed",
    AppointmentErrorCode.APPOINTMENT_CANNOT_CANCEL: "Cannot cancel this appointment",
    AppointmentErrorCode.APPOINTMENT_CANNOT_RESCHEDULE: "Cannot reschedule this appointment",
    AppointmentErrorCode.APPOINTMENT_SLOT_UNAVAILABLE: "Selected time slot is not available",
    AppointmentErrorCode.APPOINTMENT_DURATION_INVALID: "Invalid appointment duration",

    # Booking errors
    BookingErrorCode.BOOKING_NOT_FOUND: "Booking not found",
    BookingErrorCode.BOOKING_ALREADY_EXISTS: "Booking already exists",
    BookingErrorCode.BOOKING_PAYMENT_FAILED: "Payment failed for booking",
    BookingErrorCode.BOOKING_REFUND_FAILED: "Refund processing failed",
    BookingErrorCode.BOOKING_INVALID_STATUS: "Invalid booking status",

    # Payment errors
    PaymentErrorCode.PAYMENT_NOT_FOUND: "Payment not found",
    PaymentErrorCode.PAYMENT_FAILED: "Payment processing failed",
    PaymentErrorCode.PAYMENT_ALREADY_PROCESSED: "Payment already processed",
    PaymentErrorCode.PAYMENT_INVALID_AMOUNT: "Invalid payment amount",
    PaymentErrorCode.PAYMENT_METHOD_INVALID: "Invalid payment method",
    PaymentErrorCode.PAYMENT_GATEWAY_ERROR: "Payment gateway error",

    # Notification errors
    NotificationErrorCode.NOTIFICATION_SEND_FAILED: "Failed to send notification",
    NotificationErrorCode.NOTIFICATION_INVALID_TEMPLATE: "Invalid notification template",
    NotificationErrorCode.NOTIFICATION_INVALID_RECIPIENT: "Invalid notification recipient",
}