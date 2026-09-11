from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4baa71a-654c-5f08-bec8-783eb80913e4',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoomex.Name',
    display_name='Houndoom ex',
    searchable_by=['Houndoom ex', 'Stage 1', 'ex', 'Houndoomex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=134,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    family_id=228,
    abilities=[
        Attack(
            title='Evil Claw',
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title="Hound's Fang",
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.DARKNESS: 3},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
