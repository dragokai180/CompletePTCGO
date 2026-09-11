from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='078d89f2-1516-55b6-b58f-b08a3f9153d5',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MSceptileEX.Name',
    display_name='M Sceptile-EX',
    searchable_by=['M Sceptile-EX', 'MEGA', 'EX', 'MSceptileEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=8,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.SceptileEX.Name',
    family_id=254,
    abilities=[
        Attack(
            title='Jagged Saber',
            game_text='You may attach up to 2 Grass Energy cards from your hand to your Benched Pokémon in any way you like. If you attached Energy to a Pokémon in this way, heal all damage from that Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
)
