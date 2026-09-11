from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a71807ad-629f-5e1b-aa33-da6b79c3f668',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name',
    display_name='Mabosstiff',
    searchable_by=['Mabosstiff', 'Stage 1', 'Mabosstiff'],
    subtypes=['Stage 1'],
    collector_number=143,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name',
    family_id=942,
    abilities=[
        Attack(
            title='Comeuppance',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack\xa0(even if it is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Darkness Fang',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
