from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e4e09b9-2f34-5513-992b-9b3fd4643e63',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name',
    display_name='Escavalier',
    searchable_by=['Escavalier', 'Stage 1', 'Escavalier'],
    subtypes=['Stage 1'],
    collector_number=142,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name',
    family_id=588,
    abilities=[
        Attack(
            title='Discerning Spear',
            game_text="If your opponent's Active Pokémon has no damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.METAL: 1},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Iron Lance',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
