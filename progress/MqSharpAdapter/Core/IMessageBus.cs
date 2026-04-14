public interface IMessageBus
{
    Task SendAsync<T>(string queue, T message, CancellationToken ct = default);
    Task PublishAsync<T>(string topic, T message, CancellationToken ct = default);
}