from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="8b936d58-6b48-59fd-8cfb-6e58d2b46ae0",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eternatus.Name",
    display_name="Eternatus",
    searchable_by=["Eternatus", "Basic", "Eternatus"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=890,
    abilities=[
        Attack(
            title="Shatter",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title="Power Rush",
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
