from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='648cd06f-78bb-5909-aa4a-5280e3224531',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name',
    display_name='Houndoom',
    searchable_by=['Houndoom', 'Stage 1', 'Houndoom'],
    subtypes=['Stage 1'],
    collector_number=133,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    family_id=228,
    abilities=[
        Attack(
            title='Daring Strike',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Shadow Slash',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
