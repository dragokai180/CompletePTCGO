from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0edab158-5f05-5e81-9565-505a9cb53ffa',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name',
    display_name='Tauros',
    searchable_by=['Tauros', 'Basic', 'Tauros'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=128,
    abilities=[
        Attack(
            title='Smash Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Crimson Bull',
            game_text='Flip 3 coins. This attack does 30 damage times the number of heads. Tauros is now Confused.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
