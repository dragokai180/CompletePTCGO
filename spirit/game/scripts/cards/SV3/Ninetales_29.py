from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f89bd162-723f-5e70-98a9-6ee337079644',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name',
    display_name='Ninetales',
    searchable_by=['Ninetales', 'Stage 1', 'Ninetales'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    family_id=37,
    abilities=[
        Attack(
            title='Will-O-Wisp',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title='Nine-Tailed Dance',
            game_text="Put 9 damage counters on 1 of your opponent's Pokémon. During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 2},
            effect=standard_attack,
        ),
    ],
)
