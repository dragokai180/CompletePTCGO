from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7e3b790b-a5d2-555a-8a4b-81c7328f0065',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name',
    display_name='Drifblim',
    searchable_by=['Drifblim', 'Stage 1', 'Drifblim'],
    subtypes=['Stage 1'],
    collector_number=90,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    family_id=425,
    abilities=[
        Attack(
            title='Gust',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Curse Spreading',
            game_text="Put 8 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=standard_attack,
        ),
    ],
)
