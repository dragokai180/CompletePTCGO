from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9e551fe8-eb2d-5314-9ef7-cfb5e64c7d41',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name',
    display_name='Furfrou',
    searchable_by=['Furfrou', 'Basic', 'Furfrou'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=676,
    abilities=[
        Attack(
            title='Tight Jaw',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
