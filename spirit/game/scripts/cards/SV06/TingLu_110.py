from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="7e8ce22b-bc0e-5bc4-8cc5-9073d327fa36",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLu.Name",
    display_name="Ting-Lu",
    searchable_by=["Ting-Lu", "Basic", "TingLu"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=1003,
    abilities=[
        Attack(
            title="Ground Crasher",
            game_text="If a Stadium is in play, this attack also does 30 damage to each of your opponent's Benched Pokémon, and discard that Stadium. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
