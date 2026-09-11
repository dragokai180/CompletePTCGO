from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a31e42b5-278a-524c-bd41-cf606835636e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name',
    display_name='Metagross',
    searchable_by=['Metagross', 'Stage 2', 'Metagross'],
    subtypes=['Stage 2'],
    collector_number=95,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    family_id=374,
    abilities=[
        Ability(
            title='Extend',
            game_text="As long as this Pokémon is your Active Pokémon, your turn does not end when you play Steven's Resolve.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your turn does not end when you play Steven's Resolve."),
        ),
        Attack(
            title='Meteor Mash',
            game_text="During your next turn, this Pokémon's Meteor Mash attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
