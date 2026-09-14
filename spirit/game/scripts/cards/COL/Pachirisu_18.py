from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c4ba181d-e00f-5814-9a58-9a894adb60b6',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name',
    display_name='Pachirisu',
    searchable_by=['Pachirisu', 'Basic', 'Pachirisu'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=417,
    abilities=[
        Ability(
            title='Self-Generation',
            game_text='Once during your turn, when you put Pachirisu from your hand onto your Bench, you may attach up to 2 Lightning Energy cards from your hand to Pachirisu.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Shocking Bolt',
            game_text='Put all Energy cards attached to Pachirisu in the Lost Zone.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
