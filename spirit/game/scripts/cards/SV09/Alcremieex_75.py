from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="38ba9c4f-08d4-579e-9f4b-d32d92e86277",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremieex.Name",
    display_name="Alcremie ex",
    searchable_by=["Alcremie ex", "Stage 1", "ex", "Alcremieex"],
    subtypes=["Stage 1", "ex"],
    collector_number=75,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Ability(
            title="Confectionary Gift",
            game_text="Once during your turn, you may heal 30 damage from 1 of your Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Whipped Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
