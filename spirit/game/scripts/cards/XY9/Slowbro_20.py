from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7edd005c-7b69-5290-93dc-463a99b4721c',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name',
    display_name='Slowbro',
    searchable_by=['Slowbro', 'Stage 1', 'Slowbro'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Attack(
            title='Careless Head',
            game_text='Flip a coin. If heads, this attack does 50 more damage.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Walk-Off Homer',
            game_text='If you use this attack when you have only 1 Prize card left, you win this game.',
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
