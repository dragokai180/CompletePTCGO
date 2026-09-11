from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='738e6e99-9d50-54ea-a457-289fe0a5a131',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name',
    display_name='Ledyba',
    searchable_by=['Ledyba', 'Basic', 'Ledyba'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=165,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Comet Punch',
            game_text='Flip 4 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
