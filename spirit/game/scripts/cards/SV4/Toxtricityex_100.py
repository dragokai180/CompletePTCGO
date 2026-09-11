from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='7eae81ae-5447-5a69-b306-6697b76b1b21',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricityex.Name',
    display_name='Toxtricity ex',
    searchable_by=['Toxtricity ex', 'Stage 1', 'Tera', 'ex', 'Toxtricityex'],
    subtypes=['Stage 1', 'Tera', 'ex'],
    collector_number=100,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name',
    family_id=848,
    abilities=[
        Attack(
            title='Knocking Hammer',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Gaia Punk',
            game_text='Discard 3 Lightning Energy from your Pokémon.',
            cost={PokemonTypes.LIGHTNING: 3},
            damage=270,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
