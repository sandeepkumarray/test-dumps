public interface IMessageHandler<T>
{
    Task HandleAsync(T message, CancellationToken ct);
}