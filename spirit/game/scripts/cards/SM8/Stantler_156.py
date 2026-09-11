from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df2d2e41-c329-5b8e-a19e-6c3c0a70a987',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name',
    display_name='Stantler',
    searchable_by=['Stantler', 'Basic', 'Stantler'],
    subtypes=['Basic'],
    collector_number=156,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=234,
    abilities=[
        Attack(
            title='Mystifying Horns',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Enhanced Horns',
            game_text='If this Pokémon has a Pokémon Tool card attached to it, this attack does 60 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
