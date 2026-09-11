from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bd6432f-f2cb-5b4b-8f67-204d260639b1',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name',
    display_name='Whimsicott',
    searchable_by=['Whimsicott', 'Stage 1', 'Whimsicott'],
    subtypes=['Stage 1'],
    collector_number=148,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
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
            title='Sneaky Pocket',
            game_text='Put a card from your hand in the Lost Zone. If you do, draw 3 cards.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Lost March',
            game_text='This attack does 20 damage for each of your Pokémon, except p (Prism Star) Pokémon, in the Lost Zone.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
