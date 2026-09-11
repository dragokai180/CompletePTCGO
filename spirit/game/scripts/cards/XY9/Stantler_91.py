from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='81aed745-5abf-53ce-9990-91916866b733',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name',
    display_name='Stantler',
    searchable_by=['Stantler', 'Basic', 'Stantler'],
    subtypes=['Basic'],
    collector_number=91,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=234,
    abilities=[
        Attack(
            title='Mystifying Horns',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Big Charge',
            game_text='If you have any Mega Evolution Pokémon on your Bench, this attack does 50 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
