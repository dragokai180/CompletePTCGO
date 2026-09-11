from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='31eca897-3558-5602-bc5a-04b3276dd8d0',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name',
    display_name='Type: Null',
    searchable_by=['Type: Null', 'Basic', 'TypeNull'],
    subtypes=['Basic'],
    collector_number=115,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=772,
    abilities=[
        Attack(
            title='Merciless Strike',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Headbang',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
