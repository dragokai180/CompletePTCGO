from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="0dca2680-1156-591a-a0e0-6117fdf672aa",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansPinsir.Name",
    display_name="Ethan's Pinsir",
    searchable_by=["Ethan's Pinsir", "Basic", "EthansPinsir"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=127,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Rallying Horn",
            game_text="If any of your Ethan's Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
