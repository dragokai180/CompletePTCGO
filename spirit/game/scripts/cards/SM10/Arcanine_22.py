from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6fd3b827-ae03-5b34-b6fd-c569485c076c',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name',
    display_name='Arcanine',
    searchable_by=['Arcanine', 'Stage 1', 'Arcanine'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    family_id=58,
    abilities=[
        Attack(
            title='Grand Flame',
            game_text='Attach 2 Fire Energy cards from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIRE: 3},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Heat Tackle',
            game_text='This Pokémon does 50 damage to itself.',
            cost={PokemonTypes.FIRE: 4},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
