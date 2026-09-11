from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1a47c7a-7e4f-5d82-9d8b-4c7fe71c6343',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name',
    display_name='Dragonite',
    searchable_by=['Dragonite', 'Stage 2', 'Dragonite'],
    subtypes=['Stage 2'],
    collector_number=52,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Wrapped in Wind',
            game_text='Attach up to 2 basic Energy cards from your hand to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.GRASS: 3, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
    passive=standard_passive("If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card."),
)
