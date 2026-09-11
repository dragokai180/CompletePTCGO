from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4cbff1a-9a63-55f8-bc7c-dea3047e5db0',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name',
    display_name='Cyclizar',
    searchable_by=['Cyclizar', 'Basic', 'Cyclizar'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=967,
    abilities=[
        Attack(
            title='Acceleration Drive',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
