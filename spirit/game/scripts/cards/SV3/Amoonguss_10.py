from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad603eca-71a9-5b25-91e6-bd62dead4377',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name',
    display_name='Amoonguss',
    searchable_by=['Amoonguss', 'Stage 1', 'Amoonguss'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name',
    family_id=590,
    abilities=[
        Attack(
            title='Dangerous Spores',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
