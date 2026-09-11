from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='12f697d0-0fca-5c77-a96f-71d91a1bfc8d',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name',
    display_name='Granbull',
    searchable_by=['Granbull', 'Stage 1', 'Granbull'],
    subtypes=['Stage 1'],
    collector_number=88,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name',
    family_id=209,
    abilities=[
        Attack(
            title='Confront',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Wild Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
