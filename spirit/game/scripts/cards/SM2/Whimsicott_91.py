from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4459670-cc29-58e9-82a2-e010e4fceba2',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name',
    display_name='Whimsicott',
    searchable_by=['Whimsicott', 'Stage 1', 'Whimsicott'],
    subtypes=['Stage 1'],
    collector_number=91,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    family_id=546,
    abilities=[
        Attack(
            title='The Wages of Fluff',
            game_text='If the Defending Pokémon is Knocked Out during your next turn, take 2 more Prize cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
        ),
    ],
)
