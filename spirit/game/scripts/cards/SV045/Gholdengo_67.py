from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd67cfde-bcdd-5320-97a1-1ed397393200',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gholdengo.Name',
    display_name='Gholdengo',
    searchable_by=['Gholdengo', 'Stage 1', 'Gholdengo'],
    subtypes=['Stage 1'],
    collector_number=67,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name',
    family_id=999,
    abilities=[
        Attack(
            title='Lavish Hospitality',
            game_text='You may attach any number of Basic Metal Energy cards from your hand to your Pokémon in any way you like.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scintillating Surfing',
            game_text='Flip a coin for each Metal Energy attached to this Pokémon. This attack does 80 damage for each heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
