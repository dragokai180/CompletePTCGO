from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='23b02669-c934-5ed1-8d1c-85068646dd6a',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name',
    display_name='Dragonite-EX',
    searchable_by=['Dragonite-EX', 'Basic', 'EX', 'DragoniteEX'],
    subtypes=['Basic', 'EX'],
    collector_number=74,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=149,
    abilities=[
        Ability(
            title='Bust In',
            game_text='When you play this Pokémon from your hand onto your Bench, you may move any number of basic Energy attached to your Pokémon to this Pokémon. If you do, switch this Pokémon with your Active Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Jet Sonic',
            game_text='You may discard an Energy attached to this Pokémon. If you do, this attack does 40 more damage.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.LIGHTNING: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
