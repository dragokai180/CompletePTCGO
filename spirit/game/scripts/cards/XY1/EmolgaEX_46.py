from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='256fe356-5a0a-5782-b2ae-f06a273ab98c',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.EmolgaEX.Name',
    display_name='Emolga-EX',
    searchable_by=['Emolga-EX', 'Basic', 'EX', 'EmolgaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=46,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=587,
    abilities=[
        Attack(
            title='Energy Glide',
            game_text='Search your deck for a Lightning Energy card and attach it to this Pokémon. Shuffle your deck afterward. If you attached Energy in this way, switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electron Crush',
            game_text='You may discard an Energy attached to this Pokémon. If you do, this attack does 30 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
