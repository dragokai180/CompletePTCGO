from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def top_down(ctx):
    """80. Flip a coin until you get tails. For each heads, discard the top
    card of your opponent's deck."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails(ctx.ability.title)
    if heads:
        await ctx.discard_cards(ctx.deck_top(heads, player_id=ctx.opponent_id))



card = PokemonCardDef(
    guid="1571784c-d8fb-5211-9f69-23a8a874a394",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr","Stage 2","Conkeldurr"],
    subtypes=["Stage 2"],
    collector_number=64,
    set_code="BW3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    abilities=[
        Ability(
            title="Craftsmanship",
            game_text="This Pokémon gets +20 HP for each Fighting Energy attached to it.",
            passive=bw_legacy_passive("This Pokémon gets +20 HP for each Fighting Energy attached to it."),
        ),
        Attack(
            title="Top Down",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=top_down,
        ),
    ],
)
