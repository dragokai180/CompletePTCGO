from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='08a98e17-f90d-5794-9d64-fccd28bf631a',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    display_name='Onix',
    searchable_by=['Onix', 'Basic', 'Onix'],
    subtypes=['Basic'],
    collector_number=95,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=95,
    abilities=[
        Attack(
            title='Thumpalanche',
            game_text='Discard the top 5 cards of your deck. This attack does 80 damage for each Pokémon with a Retreat Cost of exactly 4 that you discarded in this way.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
