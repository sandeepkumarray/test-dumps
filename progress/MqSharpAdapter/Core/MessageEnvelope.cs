public class MessageEnvelope<T>
{
    public T Payload { get; set; } = default!;
    public string MessageId { get; set; } = Guid.NewGuid().ToString();
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
}