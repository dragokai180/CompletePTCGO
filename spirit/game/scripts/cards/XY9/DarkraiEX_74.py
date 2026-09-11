from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a3fcc9f0-e1c7-5521-87e8-c0eaef560158',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiEX.Name',
    display_name='Darkrai-EX',
    searchable_by=['Darkrai-EX', 'Basic', 'EX', 'DarkraiEX'],
    subtypes=['Basic', 'EX'],
    collector_number=74,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Attack(
            title='Dark Pulse',
            game_text='This attack does 20 more damage for each Darkness Energy attached to all of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dark Head',
            game_text="If your opponent's Active Pokémon is Asleep, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
