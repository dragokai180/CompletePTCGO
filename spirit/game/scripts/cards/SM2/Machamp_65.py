from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='84cb8e69-31ff-5d86-90d2-a31a2479c23b',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name',
    display_name='Machamp',
    searchable_by=['Machamp', 'Stage 2', 'Machamp'],
    subtypes=['Stage 2'],
    collector_number=65,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name',
    family_id=66,
    abilities=[
        Attack(
            title='Settle the Score',
            game_text='This attack does 80 more damage for each Prize card your opponent took on their last turn.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Submission',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
