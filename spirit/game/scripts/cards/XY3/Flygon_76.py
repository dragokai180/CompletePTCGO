from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9999aee0-8e7d-5f09-912f-5eee510f8325',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name',
    display_name='Flygon',
    searchable_by=['Flygon', 'Stage 2', 'Flygon'],
    subtypes=['Stage 2'],
    collector_number=76,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name',
    family_id=328,
    abilities=[
        Attack(
            title='Rainbow Shower',
            game_text='Attach as many basic Energy cards as you like from your hand to your Pokémon in any way you like.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sand Sweep',
            game_text='Heal 30 damage from each of your Pokémon that has any Energy attached to it.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
