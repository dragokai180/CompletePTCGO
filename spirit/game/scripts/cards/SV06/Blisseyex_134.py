from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4374c765-4989-5939-8354-188c315d4c4f",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blisseyex.Name",
    display_name="Blissey ex",
    searchable_by=["Blissey ex", "Stage 1", "ex", "Blisseyex"],
    subtypes=["Stage 1", "ex"],
    collector_number=134,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Happy Switch",
            game_text="Once during your turn, you may move a Basic Energy from 1 of your Pokémon to another of your Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
