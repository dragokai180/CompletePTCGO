from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec9b782e-cdb3-5f69-8677-dfbc28b2a0e6',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name',
    display_name='Ninetales',
    searchable_by=['Ninetales', 'Stage 1', 'Ninetales'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    family_id=37,
    abilities=[
        Ability(
            title='Barrier Shrine',
            game_text="Each player can't play any Stadium cards from his or her hand.",
            passive=standard_passive("Each player can't play any Stadium cards from his or her hand."),
        ),
        Attack(
            title='Flickering Flames',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
