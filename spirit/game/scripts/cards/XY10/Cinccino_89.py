from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55a8b93a-de28-5849-a9c1-6e4d9dc03fb8',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name',
    display_name='Cinccino',
    searchable_by=['Cinccino', 'Stage 1', 'Cinccino'],
    subtypes=['Stage 1'],
    collector_number=89,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name',
    family_id=572,
    abilities=[
        Attack(
            title='Sweeping Cure',
            game_text='Heal 90 damage from 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
