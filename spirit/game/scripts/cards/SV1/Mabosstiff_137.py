from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8619ac4c-20a1-5c1d-8ab0-ae88e1bf5133',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name',
    display_name='Mabosstiff',
    searchable_by=['Mabosstiff', 'Stage 1', 'Mabosstiff'],
    subtypes=['Stage 1'],
    collector_number=137,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name',
    family_id=942,
    abilities=[
        Ability(
            title='Intimidating Howl',
            game_text="Once during your turn, you may switch out your opponent's Active Pokémon to the Bench.\xa0(Your opponent chooses the new Active Pokémon.)",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Wild Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
