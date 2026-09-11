from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="549ccdf5-dd4d-56c7-8b89-29d4a5c009de",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaEmboarex.Name",
    display_name="Mega Emboar ex",
    searchable_by=["Mega Emboar ex", "Stage 2", "MEGA", "ex", "SV_Mega", "MegaEmboarex"],
    subtypes=["Stage 2", "MEGA", "ex", "SV_Mega"],
    collector_number=31,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=380,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Crimson Blast",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=320,
            effect=standard_attack,
        ),
    ],
)
