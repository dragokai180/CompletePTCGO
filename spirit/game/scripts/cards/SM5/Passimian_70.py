from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0e8b2e70-f5fe-5c93-9a9e-2afc21c8fca7',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name',
    display_name='Passimian',
    searchable_by=['Passimian', 'Basic', 'Passimian'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=766,
    abilities=[
        Ability(
            title='Power Huddle',
            game_text="As long as this Pokémon is on your Bench, your Passimian's attacks do 30 more damage to your opponent's Active Evolution Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is on your Bench, your Passimian's attacks do 30 more damage to your opponent's Active Evolution Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Rock Hurl',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
