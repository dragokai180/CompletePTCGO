from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='96f39784-41ec-55bd-8438-84db33e545fc',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dondozo.Name',
    display_name='Dondozo',
    searchable_by=['Dondozo', 'Basic', 'Dondozo'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=977,
    abilities=[
        Attack(
            title='Release Rage',
            game_text='This attack does 50 damage for each Tatsugiri in your discard pile.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Splash',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
