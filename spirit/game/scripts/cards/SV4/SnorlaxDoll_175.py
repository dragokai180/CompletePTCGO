from spirit.game.data_utils import Ability, Activations, FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_passive,
)


_TEXT = "If this card is in your hand when you are setting up to play, you may put it face down in the Active Spot or on your Bench as if it were a 120-HP Basic Colorless Pokémon. (You can do this only when you are setting up to play.) At any time during your turn, you may discard this card from play. This card can't be affected by any Special Conditions and can't retreat. If this card is Knocked Out, your opponent can't take any Prize cards for it."

card = FossilItemCardDef(
    guid='aaf07932-b23c-5bb4-b07e-6cc6ce100152',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SnorlaxDoll.Name',
    display_name='Snorlax Doll',
    searchable_by=['Snorlax Doll', 'Item', 'SnorlaxDoll'],
    subtypes=['Item'],
    collector_number=175,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    passive=standard_passive(_TEXT),
    setup_as_active=True,
    setup_as_bench=True,
    unplayable_from_hand=True,
    abilities=[Ability(
        title="Discard Snorlax Doll",
        game_text=_TEXT,
        effect=standard_ability,
        activation=Activations.UNLIMITED,
    )],
)
