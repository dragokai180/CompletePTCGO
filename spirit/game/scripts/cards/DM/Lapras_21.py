from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d82eb6fb-ea70-5a1f-b893-d6dc299a43fe',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name',
    display_name='Lapras',
    searchable_by=['Lapras', 'Basic', 'Lapras'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=131,
    abilities=[
        Attack(
            title='Aqua Bullet',
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 10 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
