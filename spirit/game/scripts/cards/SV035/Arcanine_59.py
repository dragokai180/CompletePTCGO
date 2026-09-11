from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='07ef02d0-b382-55e6-9405-8f6888fbe500',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name',
    display_name='Arcanine',
    searchable_by=['Arcanine', 'Stage 1', 'Arcanine'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    family_id=58,
    abilities=[
        Attack(
            title='Torrid Torrent',
            game_text='Attach up to 2 Basic Fire Energy cards from your discard pile to this Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Dynamite Fang',
            game_text='Discard 2 Fire Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=240,
            effect=standard_attack,
        ),
    ],
)
