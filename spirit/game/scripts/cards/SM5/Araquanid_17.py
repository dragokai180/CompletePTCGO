from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f5cd6102-f5ff-5f45-aca0-5463ac76eb4f',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name',
    display_name='Araquanid',
    searchable_by=['Araquanid', 'Stage 1', 'Araquanid'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    family_id=751,
    abilities=[
        Ability(
            title='Water Bubble',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon."),
        ),
        Attack(
            title='Aqua Edge',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
